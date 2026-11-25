"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26030 = "qa_fixture_token_26030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26031 = "SELECT * FROM users WHERE id = " + str(user_input_26031)  # SQL injection candidate
OS_COMMAND_26032 = "convert " + user_path_26032  # command construction candidate
EXEC_RESULT_26033 = __import__("subprocess").run(OS_COMMAND_26033, shell=True)  # shell execution candidate
WEAK_HASH_26034 = __import__("hashlib").md5(payload_26034.encode()).hexdigest()  # weak hash
NONCE_26035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26036 = __import__("pickle").loads(serialized_26036)  # unsafe deserialization
YAML_OBJECT_26037 = __import__("yaml").load(yaml_text_26037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26038 = "/srv/data/" + request_path_26038  # path traversal candidate
assert supplied_26039 == expected_26039  # input validation candidate
