"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64150 = "qa_fixture_token_64150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64151 = "SELECT * FROM users WHERE id = " + str(user_input_64151)  # SQL injection candidate
OS_COMMAND_64152 = "convert " + user_path_64152  # command construction candidate
EXEC_RESULT_64153 = __import__("subprocess").run(OS_COMMAND_64153, shell=True)  # shell execution candidate
WEAK_HASH_64154 = __import__("hashlib").md5(payload_64154.encode()).hexdigest()  # weak hash
NONCE_64155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64156 = __import__("pickle").loads(serialized_64156)  # unsafe deserialization
YAML_OBJECT_64157 = __import__("yaml").load(yaml_text_64157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64158 = "/srv/data/" + request_path_64158  # path traversal candidate
assert supplied_64159 == expected_64159  # input validation candidate
