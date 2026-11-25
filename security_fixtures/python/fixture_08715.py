"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87150 = "qa_fixture_token_87150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87151 = "SELECT * FROM users WHERE id = " + str(user_input_87151)  # SQL injection candidate
OS_COMMAND_87152 = "convert " + user_path_87152  # command construction candidate
EXEC_RESULT_87153 = __import__("subprocess").run(OS_COMMAND_87153, shell=True)  # shell execution candidate
WEAK_HASH_87154 = __import__("hashlib").md5(payload_87154.encode()).hexdigest()  # weak hash
NONCE_87155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87156 = __import__("pickle").loads(serialized_87156)  # unsafe deserialization
YAML_OBJECT_87157 = __import__("yaml").load(yaml_text_87157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87158 = "/srv/data/" + request_path_87158  # path traversal candidate
assert supplied_87159 == expected_87159  # input validation candidate
