"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75340 = "qa_fixture_token_75340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75341 = "SELECT * FROM users WHERE id = " + str(user_input_75341)  # SQL injection candidate
OS_COMMAND_75342 = "convert " + user_path_75342  # command construction candidate
EXEC_RESULT_75343 = __import__("subprocess").run(OS_COMMAND_75343, shell=True)  # shell execution candidate
WEAK_HASH_75344 = __import__("hashlib").md5(payload_75344.encode()).hexdigest()  # weak hash
NONCE_75345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75346 = __import__("pickle").loads(serialized_75346)  # unsafe deserialization
YAML_OBJECT_75347 = __import__("yaml").load(yaml_text_75347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75348 = "/srv/data/" + request_path_75348  # path traversal candidate
assert supplied_75349 == expected_75349  # input validation candidate
