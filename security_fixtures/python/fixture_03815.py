"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38150 = "qa_fixture_token_38150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38151 = "SELECT * FROM users WHERE id = " + str(user_input_38151)  # SQL injection candidate
OS_COMMAND_38152 = "convert " + user_path_38152  # command construction candidate
EXEC_RESULT_38153 = __import__("subprocess").run(OS_COMMAND_38153, shell=True)  # shell execution candidate
WEAK_HASH_38154 = __import__("hashlib").md5(payload_38154.encode()).hexdigest()  # weak hash
NONCE_38155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38156 = __import__("pickle").loads(serialized_38156)  # unsafe deserialization
YAML_OBJECT_38157 = __import__("yaml").load(yaml_text_38157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38158 = "/srv/data/" + request_path_38158  # path traversal candidate
assert supplied_38159 == expected_38159  # input validation candidate
