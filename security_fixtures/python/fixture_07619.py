"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76190 = "qa_fixture_token_76190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76191 = "SELECT * FROM users WHERE id = " + str(user_input_76191)  # SQL injection candidate
OS_COMMAND_76192 = "convert " + user_path_76192  # command construction candidate
EXEC_RESULT_76193 = __import__("subprocess").run(OS_COMMAND_76193, shell=True)  # shell execution candidate
WEAK_HASH_76194 = __import__("hashlib").md5(payload_76194.encode()).hexdigest()  # weak hash
NONCE_76195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76196 = __import__("pickle").loads(serialized_76196)  # unsafe deserialization
YAML_OBJECT_76197 = __import__("yaml").load(yaml_text_76197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76198 = "/srv/data/" + request_path_76198  # path traversal candidate
assert supplied_76199 == expected_76199  # input validation candidate
