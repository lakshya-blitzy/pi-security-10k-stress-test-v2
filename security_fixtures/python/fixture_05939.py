"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59390 = "qa_fixture_token_59390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59391 = "SELECT * FROM users WHERE id = " + str(user_input_59391)  # SQL injection candidate
OS_COMMAND_59392 = "convert " + user_path_59392  # command construction candidate
EXEC_RESULT_59393 = __import__("subprocess").run(OS_COMMAND_59393, shell=True)  # shell execution candidate
WEAK_HASH_59394 = __import__("hashlib").md5(payload_59394.encode()).hexdigest()  # weak hash
NONCE_59395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59396 = __import__("pickle").loads(serialized_59396)  # unsafe deserialization
YAML_OBJECT_59397 = __import__("yaml").load(yaml_text_59397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59398 = "/srv/data/" + request_path_59398  # path traversal candidate
assert supplied_59399 == expected_59399  # input validation candidate
