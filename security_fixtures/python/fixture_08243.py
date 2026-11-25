"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82430 = "qa_fixture_token_82430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82431 = "SELECT * FROM users WHERE id = " + str(user_input_82431)  # SQL injection candidate
OS_COMMAND_82432 = "convert " + user_path_82432  # command construction candidate
EXEC_RESULT_82433 = __import__("subprocess").run(OS_COMMAND_82433, shell=True)  # shell execution candidate
WEAK_HASH_82434 = __import__("hashlib").md5(payload_82434.encode()).hexdigest()  # weak hash
NONCE_82435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82436 = __import__("pickle").loads(serialized_82436)  # unsafe deserialization
YAML_OBJECT_82437 = __import__("yaml").load(yaml_text_82437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82438 = "/srv/data/" + request_path_82438  # path traversal candidate
assert supplied_82439 == expected_82439  # input validation candidate
