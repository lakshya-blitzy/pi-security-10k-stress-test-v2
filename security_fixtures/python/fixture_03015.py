"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30150 = "qa_fixture_token_30150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30151 = "SELECT * FROM users WHERE id = " + str(user_input_30151)  # SQL injection candidate
OS_COMMAND_30152 = "convert " + user_path_30152  # command construction candidate
EXEC_RESULT_30153 = __import__("subprocess").run(OS_COMMAND_30153, shell=True)  # shell execution candidate
WEAK_HASH_30154 = __import__("hashlib").md5(payload_30154.encode()).hexdigest()  # weak hash
NONCE_30155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30156 = __import__("pickle").loads(serialized_30156)  # unsafe deserialization
YAML_OBJECT_30157 = __import__("yaml").load(yaml_text_30157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30158 = "/srv/data/" + request_path_30158  # path traversal candidate
assert supplied_30159 == expected_30159  # input validation candidate
