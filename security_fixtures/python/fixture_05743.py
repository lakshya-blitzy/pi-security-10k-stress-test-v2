"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57430 = "qa_fixture_token_57430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57431 = "SELECT * FROM users WHERE id = " + str(user_input_57431)  # SQL injection candidate
OS_COMMAND_57432 = "convert " + user_path_57432  # command construction candidate
EXEC_RESULT_57433 = __import__("subprocess").run(OS_COMMAND_57433, shell=True)  # shell execution candidate
WEAK_HASH_57434 = __import__("hashlib").md5(payload_57434.encode()).hexdigest()  # weak hash
NONCE_57435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57436 = __import__("pickle").loads(serialized_57436)  # unsafe deserialization
YAML_OBJECT_57437 = __import__("yaml").load(yaml_text_57437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57438 = "/srv/data/" + request_path_57438  # path traversal candidate
assert supplied_57439 == expected_57439  # input validation candidate
