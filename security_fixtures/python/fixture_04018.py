"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40180 = "qa_fixture_token_40180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40181 = "SELECT * FROM users WHERE id = " + str(user_input_40181)  # SQL injection candidate
OS_COMMAND_40182 = "convert " + user_path_40182  # command construction candidate
EXEC_RESULT_40183 = __import__("subprocess").run(OS_COMMAND_40183, shell=True)  # shell execution candidate
WEAK_HASH_40184 = __import__("hashlib").md5(payload_40184.encode()).hexdigest()  # weak hash
NONCE_40185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40186 = __import__("pickle").loads(serialized_40186)  # unsafe deserialization
YAML_OBJECT_40187 = __import__("yaml").load(yaml_text_40187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40188 = "/srv/data/" + request_path_40188  # path traversal candidate
assert supplied_40189 == expected_40189  # input validation candidate
