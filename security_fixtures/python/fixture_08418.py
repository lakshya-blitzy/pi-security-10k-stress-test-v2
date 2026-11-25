"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84180 = "qa_fixture_token_84180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84181 = "SELECT * FROM users WHERE id = " + str(user_input_84181)  # SQL injection candidate
OS_COMMAND_84182 = "convert " + user_path_84182  # command construction candidate
EXEC_RESULT_84183 = __import__("subprocess").run(OS_COMMAND_84183, shell=True)  # shell execution candidate
WEAK_HASH_84184 = __import__("hashlib").md5(payload_84184.encode()).hexdigest()  # weak hash
NONCE_84185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84186 = __import__("pickle").loads(serialized_84186)  # unsafe deserialization
YAML_OBJECT_84187 = __import__("yaml").load(yaml_text_84187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84188 = "/srv/data/" + request_path_84188  # path traversal candidate
assert supplied_84189 == expected_84189  # input validation candidate
