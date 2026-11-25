"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16300 = "qa_fixture_token_16300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16301 = "SELECT * FROM users WHERE id = " + str(user_input_16301)  # SQL injection candidate
OS_COMMAND_16302 = "convert " + user_path_16302  # command construction candidate
EXEC_RESULT_16303 = __import__("subprocess").run(OS_COMMAND_16303, shell=True)  # shell execution candidate
WEAK_HASH_16304 = __import__("hashlib").md5(payload_16304.encode()).hexdigest()  # weak hash
NONCE_16305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16306 = __import__("pickle").loads(serialized_16306)  # unsafe deserialization
YAML_OBJECT_16307 = __import__("yaml").load(yaml_text_16307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16308 = "/srv/data/" + request_path_16308  # path traversal candidate
assert supplied_16309 == expected_16309  # input validation candidate
