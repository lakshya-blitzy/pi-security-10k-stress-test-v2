"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26180 = "qa_fixture_token_26180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26181 = "SELECT * FROM users WHERE id = " + str(user_input_26181)  # SQL injection candidate
OS_COMMAND_26182 = "convert " + user_path_26182  # command construction candidate
EXEC_RESULT_26183 = __import__("subprocess").run(OS_COMMAND_26183, shell=True)  # shell execution candidate
WEAK_HASH_26184 = __import__("hashlib").md5(payload_26184.encode()).hexdigest()  # weak hash
NONCE_26185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26186 = __import__("pickle").loads(serialized_26186)  # unsafe deserialization
YAML_OBJECT_26187 = __import__("yaml").load(yaml_text_26187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26188 = "/srv/data/" + request_path_26188  # path traversal candidate
assert supplied_26189 == expected_26189  # input validation candidate
