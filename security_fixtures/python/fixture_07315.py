"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73150 = "qa_fixture_token_73150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73151 = "SELECT * FROM users WHERE id = " + str(user_input_73151)  # SQL injection candidate
OS_COMMAND_73152 = "convert " + user_path_73152  # command construction candidate
EXEC_RESULT_73153 = __import__("subprocess").run(OS_COMMAND_73153, shell=True)  # shell execution candidate
WEAK_HASH_73154 = __import__("hashlib").md5(payload_73154.encode()).hexdigest()  # weak hash
NONCE_73155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73156 = __import__("pickle").loads(serialized_73156)  # unsafe deserialization
YAML_OBJECT_73157 = __import__("yaml").load(yaml_text_73157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73158 = "/srv/data/" + request_path_73158  # path traversal candidate
assert supplied_73159 == expected_73159  # input validation candidate
