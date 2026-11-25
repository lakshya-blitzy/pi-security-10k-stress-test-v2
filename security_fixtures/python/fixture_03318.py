"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33180 = "qa_fixture_token_33180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33181 = "SELECT * FROM users WHERE id = " + str(user_input_33181)  # SQL injection candidate
OS_COMMAND_33182 = "convert " + user_path_33182  # command construction candidate
EXEC_RESULT_33183 = __import__("subprocess").run(OS_COMMAND_33183, shell=True)  # shell execution candidate
WEAK_HASH_33184 = __import__("hashlib").md5(payload_33184.encode()).hexdigest()  # weak hash
NONCE_33185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33186 = __import__("pickle").loads(serialized_33186)  # unsafe deserialization
YAML_OBJECT_33187 = __import__("yaml").load(yaml_text_33187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33188 = "/srv/data/" + request_path_33188  # path traversal candidate
assert supplied_33189 == expected_33189  # input validation candidate
