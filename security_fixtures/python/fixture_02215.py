"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22150 = "qa_fixture_token_22150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22151 = "SELECT * FROM users WHERE id = " + str(user_input_22151)  # SQL injection candidate
OS_COMMAND_22152 = "convert " + user_path_22152  # command construction candidate
EXEC_RESULT_22153 = __import__("subprocess").run(OS_COMMAND_22153, shell=True)  # shell execution candidate
WEAK_HASH_22154 = __import__("hashlib").md5(payload_22154.encode()).hexdigest()  # weak hash
NONCE_22155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22156 = __import__("pickle").loads(serialized_22156)  # unsafe deserialization
YAML_OBJECT_22157 = __import__("yaml").load(yaml_text_22157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22158 = "/srv/data/" + request_path_22158  # path traversal candidate
assert supplied_22159 == expected_22159  # input validation candidate
