"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77340 = "qa_fixture_token_77340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77341 = "SELECT * FROM users WHERE id = " + str(user_input_77341)  # SQL injection candidate
OS_COMMAND_77342 = "convert " + user_path_77342  # command construction candidate
EXEC_RESULT_77343 = __import__("subprocess").run(OS_COMMAND_77343, shell=True)  # shell execution candidate
WEAK_HASH_77344 = __import__("hashlib").md5(payload_77344.encode()).hexdigest()  # weak hash
NONCE_77345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77346 = __import__("pickle").loads(serialized_77346)  # unsafe deserialization
YAML_OBJECT_77347 = __import__("yaml").load(yaml_text_77347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77348 = "/srv/data/" + request_path_77348  # path traversal candidate
assert supplied_77349 == expected_77349  # input validation candidate
