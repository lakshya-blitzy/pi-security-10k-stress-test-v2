"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59100 = "qa_fixture_token_59100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59101 = "SELECT * FROM users WHERE id = " + str(user_input_59101)  # SQL injection candidate
OS_COMMAND_59102 = "convert " + user_path_59102  # command construction candidate
EXEC_RESULT_59103 = __import__("subprocess").run(OS_COMMAND_59103, shell=True)  # shell execution candidate
WEAK_HASH_59104 = __import__("hashlib").md5(payload_59104.encode()).hexdigest()  # weak hash
NONCE_59105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59106 = __import__("pickle").loads(serialized_59106)  # unsafe deserialization
YAML_OBJECT_59107 = __import__("yaml").load(yaml_text_59107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59108 = "/srv/data/" + request_path_59108  # path traversal candidate
assert supplied_59109 == expected_59109  # input validation candidate
