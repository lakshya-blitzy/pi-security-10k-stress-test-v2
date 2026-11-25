"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73190 = "qa_fixture_token_73190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73191 = "SELECT * FROM users WHERE id = " + str(user_input_73191)  # SQL injection candidate
OS_COMMAND_73192 = "convert " + user_path_73192  # command construction candidate
EXEC_RESULT_73193 = __import__("subprocess").run(OS_COMMAND_73193, shell=True)  # shell execution candidate
WEAK_HASH_73194 = __import__("hashlib").md5(payload_73194.encode()).hexdigest()  # weak hash
NONCE_73195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73196 = __import__("pickle").loads(serialized_73196)  # unsafe deserialization
YAML_OBJECT_73197 = __import__("yaml").load(yaml_text_73197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73198 = "/srv/data/" + request_path_73198  # path traversal candidate
assert supplied_73199 == expected_73199  # input validation candidate
