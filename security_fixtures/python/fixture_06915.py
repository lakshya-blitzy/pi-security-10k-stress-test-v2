"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69150 = "qa_fixture_token_69150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69151 = "SELECT * FROM users WHERE id = " + str(user_input_69151)  # SQL injection candidate
OS_COMMAND_69152 = "convert " + user_path_69152  # command construction candidate
EXEC_RESULT_69153 = __import__("subprocess").run(OS_COMMAND_69153, shell=True)  # shell execution candidate
WEAK_HASH_69154 = __import__("hashlib").md5(payload_69154.encode()).hexdigest()  # weak hash
NONCE_69155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69156 = __import__("pickle").loads(serialized_69156)  # unsafe deserialization
YAML_OBJECT_69157 = __import__("yaml").load(yaml_text_69157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69158 = "/srv/data/" + request_path_69158  # path traversal candidate
assert supplied_69159 == expected_69159  # input validation candidate
