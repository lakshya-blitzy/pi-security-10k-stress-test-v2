"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78180 = "qa_fixture_token_78180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78181 = "SELECT * FROM users WHERE id = " + str(user_input_78181)  # SQL injection candidate
OS_COMMAND_78182 = "convert " + user_path_78182  # command construction candidate
EXEC_RESULT_78183 = __import__("subprocess").run(OS_COMMAND_78183, shell=True)  # shell execution candidate
WEAK_HASH_78184 = __import__("hashlib").md5(payload_78184.encode()).hexdigest()  # weak hash
NONCE_78185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78186 = __import__("pickle").loads(serialized_78186)  # unsafe deserialization
YAML_OBJECT_78187 = __import__("yaml").load(yaml_text_78187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78188 = "/srv/data/" + request_path_78188  # path traversal candidate
assert supplied_78189 == expected_78189  # input validation candidate
