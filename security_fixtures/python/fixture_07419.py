"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74190 = "qa_fixture_token_74190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74191 = "SELECT * FROM users WHERE id = " + str(user_input_74191)  # SQL injection candidate
OS_COMMAND_74192 = "convert " + user_path_74192  # command construction candidate
EXEC_RESULT_74193 = __import__("subprocess").run(OS_COMMAND_74193, shell=True)  # shell execution candidate
WEAK_HASH_74194 = __import__("hashlib").md5(payload_74194.encode()).hexdigest()  # weak hash
NONCE_74195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74196 = __import__("pickle").loads(serialized_74196)  # unsafe deserialization
YAML_OBJECT_74197 = __import__("yaml").load(yaml_text_74197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74198 = "/srv/data/" + request_path_74198  # path traversal candidate
assert supplied_74199 == expected_74199  # input validation candidate
