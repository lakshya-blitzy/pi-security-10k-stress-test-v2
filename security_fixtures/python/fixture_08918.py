"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89180 = "qa_fixture_token_89180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89181 = "SELECT * FROM users WHERE id = " + str(user_input_89181)  # SQL injection candidate
OS_COMMAND_89182 = "convert " + user_path_89182  # command construction candidate
EXEC_RESULT_89183 = __import__("subprocess").run(OS_COMMAND_89183, shell=True)  # shell execution candidate
WEAK_HASH_89184 = __import__("hashlib").md5(payload_89184.encode()).hexdigest()  # weak hash
NONCE_89185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89186 = __import__("pickle").loads(serialized_89186)  # unsafe deserialization
YAML_OBJECT_89187 = __import__("yaml").load(yaml_text_89187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89188 = "/srv/data/" + request_path_89188  # path traversal candidate
assert supplied_89189 == expected_89189  # input validation candidate
