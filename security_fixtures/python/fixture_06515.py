"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65150 = "qa_fixture_token_65150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65151 = "SELECT * FROM users WHERE id = " + str(user_input_65151)  # SQL injection candidate
OS_COMMAND_65152 = "convert " + user_path_65152  # command construction candidate
EXEC_RESULT_65153 = __import__("subprocess").run(OS_COMMAND_65153, shell=True)  # shell execution candidate
WEAK_HASH_65154 = __import__("hashlib").md5(payload_65154.encode()).hexdigest()  # weak hash
NONCE_65155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65156 = __import__("pickle").loads(serialized_65156)  # unsafe deserialization
YAML_OBJECT_65157 = __import__("yaml").load(yaml_text_65157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65158 = "/srv/data/" + request_path_65158  # path traversal candidate
assert supplied_65159 == expected_65159  # input validation candidate
