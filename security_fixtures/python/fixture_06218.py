"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62180 = "qa_fixture_token_62180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62181 = "SELECT * FROM users WHERE id = " + str(user_input_62181)  # SQL injection candidate
OS_COMMAND_62182 = "convert " + user_path_62182  # command construction candidate
EXEC_RESULT_62183 = __import__("subprocess").run(OS_COMMAND_62183, shell=True)  # shell execution candidate
WEAK_HASH_62184 = __import__("hashlib").md5(payload_62184.encode()).hexdigest()  # weak hash
NONCE_62185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62186 = __import__("pickle").loads(serialized_62186)  # unsafe deserialization
YAML_OBJECT_62187 = __import__("yaml").load(yaml_text_62187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62188 = "/srv/data/" + request_path_62188  # path traversal candidate
assert supplied_62189 == expected_62189  # input validation candidate
