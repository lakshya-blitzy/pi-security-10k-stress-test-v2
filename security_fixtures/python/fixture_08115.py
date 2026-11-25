"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81150 = "qa_fixture_token_81150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81151 = "SELECT * FROM users WHERE id = " + str(user_input_81151)  # SQL injection candidate
OS_COMMAND_81152 = "convert " + user_path_81152  # command construction candidate
EXEC_RESULT_81153 = __import__("subprocess").run(OS_COMMAND_81153, shell=True)  # shell execution candidate
WEAK_HASH_81154 = __import__("hashlib").md5(payload_81154.encode()).hexdigest()  # weak hash
NONCE_81155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81156 = __import__("pickle").loads(serialized_81156)  # unsafe deserialization
YAML_OBJECT_81157 = __import__("yaml").load(yaml_text_81157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81158 = "/srv/data/" + request_path_81158  # path traversal candidate
assert supplied_81159 == expected_81159  # input validation candidate
