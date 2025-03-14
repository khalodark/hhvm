/**
 * Autogenerated by Thrift for thrift/compiler/test/fixtures/namespace/src/extend.thrift
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

#include <thrift/compiler/test/fixtures/namespace/gen-py3/extend/services_wrapper.h>
#include <thrift/compiler/test/fixtures/namespace/gen-py3/extend/services_api.h>
#include <thrift/lib/cpp2/async/AsyncProcessor.h>

namespace cpp2 {

ExtendTestServiceWrapper::ExtendTestServiceWrapper(PyObject *obj, folly::Executor* exc)
  : ::cpp2::HsTestServiceWrapper(obj, exc)
  {
    import_my__namespacing__extend__test__extend__services();
  }

void ExtendTestServiceWrapper::async_tm_check(
  apache::thrift::HandlerCallbackPtr<bool> callback
    , std::unique_ptr<::cpp2::HsFoo> struct1
) {
  auto ctx = callback->getRequestContext();
  folly::via(
    this->executor,
    [this, ctx,
     callback = std::move(callback),
     struct1 = std::move(struct1)
    ]() mutable {
        auto [promise, future] = folly::makePromiseContract<bool>();
        call_cy_ExtendTestService_check(
            this->if_object,
            ctx,
            std::move(promise),
            std::move(struct1)        );
        std::move(future).via(this->executor).thenTry([callback = std::move(callback)](folly::Try<bool>&& t) {
          (void)t;
          callback->complete(std::move(t));
        });
    });
}
std::shared_ptr<apache::thrift::ServerInterface> ExtendTestServiceInterface(PyObject *if_object, folly::Executor *exc) {
  return std::make_shared<ExtendTestServiceWrapper>(if_object, exc);
}
folly::SemiFuture<folly::Unit> ExtendTestServiceWrapper::semifuture_onStartServing() {
  auto [promise, future] = folly::makePromiseContract<folly::Unit>();
  call_cy_ExtendTestService_onStartServing(
      this->if_object,
      std::move(promise)
  );
  return std::move(future);
}
folly::SemiFuture<folly::Unit> ExtendTestServiceWrapper::semifuture_onStopRequested() {
  auto [promise, future] = folly::makePromiseContract<folly::Unit>();
  call_cy_ExtendTestService_onStopRequested(
      this->if_object,
      std::move(promise)
  );
  return std::move(future);
}
} // namespace cpp2
