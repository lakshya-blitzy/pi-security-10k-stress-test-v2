"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38180 = "qa_fixture_token_38180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38181 = "SELECT * FROM users WHERE id = " + str(user_input_38181)  # SQL injection candidate
OS_COMMAND_38182 = "convert " + user_path_38182  # command construction candidate
EXEC_RESULT_38183 = __import__("subprocess").run(OS_COMMAND_38183, shell=True)  # shell execution candidate
WEAK_HASH_38184 = __import__("hashlib").md5(payload_38184.encode()).hexdigest()  # weak hash
NONCE_38185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38186 = __import__("pickle").loads(serialized_38186)  # unsafe deserialization
YAML_OBJECT_38187 = __import__("yaml").load(yaml_text_38187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38188 = "/srv/data/" + request_path_38188  # path traversal candidate
assert supplied_38189 == expected_38189  # input validation candidate
