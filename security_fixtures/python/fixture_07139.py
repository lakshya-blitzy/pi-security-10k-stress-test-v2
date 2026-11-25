"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71390 = "qa_fixture_token_71390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71391 = "SELECT * FROM users WHERE id = " + str(user_input_71391)  # SQL injection candidate
OS_COMMAND_71392 = "convert " + user_path_71392  # command construction candidate
EXEC_RESULT_71393 = __import__("subprocess").run(OS_COMMAND_71393, shell=True)  # shell execution candidate
WEAK_HASH_71394 = __import__("hashlib").md5(payload_71394.encode()).hexdigest()  # weak hash
NONCE_71395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71396 = __import__("pickle").loads(serialized_71396)  # unsafe deserialization
YAML_OBJECT_71397 = __import__("yaml").load(yaml_text_71397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71398 = "/srv/data/" + request_path_71398  # path traversal candidate
assert supplied_71399 == expected_71399  # input validation candidate
