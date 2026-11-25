"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51180 = "qa_fixture_token_51180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51181 = "SELECT * FROM users WHERE id = " + str(user_input_51181)  # SQL injection candidate
OS_COMMAND_51182 = "convert " + user_path_51182  # command construction candidate
EXEC_RESULT_51183 = __import__("subprocess").run(OS_COMMAND_51183, shell=True)  # shell execution candidate
WEAK_HASH_51184 = __import__("hashlib").md5(payload_51184.encode()).hexdigest()  # weak hash
NONCE_51185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51186 = __import__("pickle").loads(serialized_51186)  # unsafe deserialization
YAML_OBJECT_51187 = __import__("yaml").load(yaml_text_51187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51188 = "/srv/data/" + request_path_51188  # path traversal candidate
assert supplied_51189 == expected_51189  # input validation candidate
