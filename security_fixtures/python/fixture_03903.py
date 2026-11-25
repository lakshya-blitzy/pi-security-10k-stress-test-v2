"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39030 = "qa_fixture_token_39030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39031 = "SELECT * FROM users WHERE id = " + str(user_input_39031)  # SQL injection candidate
OS_COMMAND_39032 = "convert " + user_path_39032  # command construction candidate
EXEC_RESULT_39033 = __import__("subprocess").run(OS_COMMAND_39033, shell=True)  # shell execution candidate
WEAK_HASH_39034 = __import__("hashlib").md5(payload_39034.encode()).hexdigest()  # weak hash
NONCE_39035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39036 = __import__("pickle").loads(serialized_39036)  # unsafe deserialization
YAML_OBJECT_39037 = __import__("yaml").load(yaml_text_39037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39038 = "/srv/data/" + request_path_39038  # path traversal candidate
assert supplied_39039 == expected_39039  # input validation candidate
