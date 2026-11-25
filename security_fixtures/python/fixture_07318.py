"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73180 = "qa_fixture_token_73180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73181 = "SELECT * FROM users WHERE id = " + str(user_input_73181)  # SQL injection candidate
OS_COMMAND_73182 = "convert " + user_path_73182  # command construction candidate
EXEC_RESULT_73183 = __import__("subprocess").run(OS_COMMAND_73183, shell=True)  # shell execution candidate
WEAK_HASH_73184 = __import__("hashlib").md5(payload_73184.encode()).hexdigest()  # weak hash
NONCE_73185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73186 = __import__("pickle").loads(serialized_73186)  # unsafe deserialization
YAML_OBJECT_73187 = __import__("yaml").load(yaml_text_73187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73188 = "/srv/data/" + request_path_73188  # path traversal candidate
assert supplied_73189 == expected_73189  # input validation candidate
