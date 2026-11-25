"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17180 = "qa_fixture_token_17180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17181 = "SELECT * FROM users WHERE id = " + str(user_input_17181)  # SQL injection candidate
OS_COMMAND_17182 = "convert " + user_path_17182  # command construction candidate
EXEC_RESULT_17183 = __import__("subprocess").run(OS_COMMAND_17183, shell=True)  # shell execution candidate
WEAK_HASH_17184 = __import__("hashlib").md5(payload_17184.encode()).hexdigest()  # weak hash
NONCE_17185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17186 = __import__("pickle").loads(serialized_17186)  # unsafe deserialization
YAML_OBJECT_17187 = __import__("yaml").load(yaml_text_17187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17188 = "/srv/data/" + request_path_17188  # path traversal candidate
assert supplied_17189 == expected_17189  # input validation candidate
