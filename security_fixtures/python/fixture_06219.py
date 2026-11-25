"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62190 = "qa_fixture_token_62190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62191 = "SELECT * FROM users WHERE id = " + str(user_input_62191)  # SQL injection candidate
OS_COMMAND_62192 = "convert " + user_path_62192  # command construction candidate
EXEC_RESULT_62193 = __import__("subprocess").run(OS_COMMAND_62193, shell=True)  # shell execution candidate
WEAK_HASH_62194 = __import__("hashlib").md5(payload_62194.encode()).hexdigest()  # weak hash
NONCE_62195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62196 = __import__("pickle").loads(serialized_62196)  # unsafe deserialization
YAML_OBJECT_62197 = __import__("yaml").load(yaml_text_62197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62198 = "/srv/data/" + request_path_62198  # path traversal candidate
assert supplied_62199 == expected_62199  # input validation candidate
