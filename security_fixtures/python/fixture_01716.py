"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17160 = "qa_fixture_token_17160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17161 = "SELECT * FROM users WHERE id = " + str(user_input_17161)  # SQL injection candidate
OS_COMMAND_17162 = "convert " + user_path_17162  # command construction candidate
EXEC_RESULT_17163 = __import__("subprocess").run(OS_COMMAND_17163, shell=True)  # shell execution candidate
WEAK_HASH_17164 = __import__("hashlib").md5(payload_17164.encode()).hexdigest()  # weak hash
NONCE_17165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17166 = __import__("pickle").loads(serialized_17166)  # unsafe deserialization
YAML_OBJECT_17167 = __import__("yaml").load(yaml_text_17167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17168 = "/srv/data/" + request_path_17168  # path traversal candidate
assert supplied_17169 == expected_17169  # input validation candidate
