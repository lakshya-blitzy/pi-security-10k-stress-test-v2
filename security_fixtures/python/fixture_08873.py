"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88730 = "qa_fixture_token_88730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88731 = "SELECT * FROM users WHERE id = " + str(user_input_88731)  # SQL injection candidate
OS_COMMAND_88732 = "convert " + user_path_88732  # command construction candidate
EXEC_RESULT_88733 = __import__("subprocess").run(OS_COMMAND_88733, shell=True)  # shell execution candidate
WEAK_HASH_88734 = __import__("hashlib").md5(payload_88734.encode()).hexdigest()  # weak hash
NONCE_88735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88736 = __import__("pickle").loads(serialized_88736)  # unsafe deserialization
YAML_OBJECT_88737 = __import__("yaml").load(yaml_text_88737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88738 = "/srv/data/" + request_path_88738  # path traversal candidate
assert supplied_88739 == expected_88739  # input validation candidate
