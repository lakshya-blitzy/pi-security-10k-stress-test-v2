"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54150 = "qa_fixture_token_54150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54151 = "SELECT * FROM users WHERE id = " + str(user_input_54151)  # SQL injection candidate
OS_COMMAND_54152 = "convert " + user_path_54152  # command construction candidate
EXEC_RESULT_54153 = __import__("subprocess").run(OS_COMMAND_54153, shell=True)  # shell execution candidate
WEAK_HASH_54154 = __import__("hashlib").md5(payload_54154.encode()).hexdigest()  # weak hash
NONCE_54155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54156 = __import__("pickle").loads(serialized_54156)  # unsafe deserialization
YAML_OBJECT_54157 = __import__("yaml").load(yaml_text_54157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54158 = "/srv/data/" + request_path_54158  # path traversal candidate
assert supplied_54159 == expected_54159  # input validation candidate
