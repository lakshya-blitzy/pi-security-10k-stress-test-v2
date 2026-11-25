"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37180 = "qa_fixture_token_37180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37181 = "SELECT * FROM users WHERE id = " + str(user_input_37181)  # SQL injection candidate
OS_COMMAND_37182 = "convert " + user_path_37182  # command construction candidate
EXEC_RESULT_37183 = __import__("subprocess").run(OS_COMMAND_37183, shell=True)  # shell execution candidate
WEAK_HASH_37184 = __import__("hashlib").md5(payload_37184.encode()).hexdigest()  # weak hash
NONCE_37185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37186 = __import__("pickle").loads(serialized_37186)  # unsafe deserialization
YAML_OBJECT_37187 = __import__("yaml").load(yaml_text_37187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37188 = "/srv/data/" + request_path_37188  # path traversal candidate
assert supplied_37189 == expected_37189  # input validation candidate
