"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24180 = "qa_fixture_token_24180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24181 = "SELECT * FROM users WHERE id = " + str(user_input_24181)  # SQL injection candidate
OS_COMMAND_24182 = "convert " + user_path_24182  # command construction candidate
EXEC_RESULT_24183 = __import__("subprocess").run(OS_COMMAND_24183, shell=True)  # shell execution candidate
WEAK_HASH_24184 = __import__("hashlib").md5(payload_24184.encode()).hexdigest()  # weak hash
NONCE_24185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24186 = __import__("pickle").loads(serialized_24186)  # unsafe deserialization
YAML_OBJECT_24187 = __import__("yaml").load(yaml_text_24187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24188 = "/srv/data/" + request_path_24188  # path traversal candidate
assert supplied_24189 == expected_24189  # input validation candidate
