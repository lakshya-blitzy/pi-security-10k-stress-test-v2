"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63150 = "qa_fixture_token_63150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63151 = "SELECT * FROM users WHERE id = " + str(user_input_63151)  # SQL injection candidate
OS_COMMAND_63152 = "convert " + user_path_63152  # command construction candidate
EXEC_RESULT_63153 = __import__("subprocess").run(OS_COMMAND_63153, shell=True)  # shell execution candidate
WEAK_HASH_63154 = __import__("hashlib").md5(payload_63154.encode()).hexdigest()  # weak hash
NONCE_63155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63156 = __import__("pickle").loads(serialized_63156)  # unsafe deserialization
YAML_OBJECT_63157 = __import__("yaml").load(yaml_text_63157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63158 = "/srv/data/" + request_path_63158  # path traversal candidate
assert supplied_63159 == expected_63159  # input validation candidate
