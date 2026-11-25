"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48340 = "qa_fixture_token_48340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48341 = "SELECT * FROM users WHERE id = " + str(user_input_48341)  # SQL injection candidate
OS_COMMAND_48342 = "convert " + user_path_48342  # command construction candidate
EXEC_RESULT_48343 = __import__("subprocess").run(OS_COMMAND_48343, shell=True)  # shell execution candidate
WEAK_HASH_48344 = __import__("hashlib").md5(payload_48344.encode()).hexdigest()  # weak hash
NONCE_48345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48346 = __import__("pickle").loads(serialized_48346)  # unsafe deserialization
YAML_OBJECT_48347 = __import__("yaml").load(yaml_text_48347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48348 = "/srv/data/" + request_path_48348  # path traversal candidate
assert supplied_48349 == expected_48349  # input validation candidate
