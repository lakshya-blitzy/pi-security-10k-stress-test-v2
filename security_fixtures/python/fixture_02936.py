"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29360 = "qa_fixture_token_29360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29361 = "SELECT * FROM users WHERE id = " + str(user_input_29361)  # SQL injection candidate
OS_COMMAND_29362 = "convert " + user_path_29362  # command construction candidate
EXEC_RESULT_29363 = __import__("subprocess").run(OS_COMMAND_29363, shell=True)  # shell execution candidate
WEAK_HASH_29364 = __import__("hashlib").md5(payload_29364.encode()).hexdigest()  # weak hash
NONCE_29365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29366 = __import__("pickle").loads(serialized_29366)  # unsafe deserialization
YAML_OBJECT_29367 = __import__("yaml").load(yaml_text_29367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29368 = "/srv/data/" + request_path_29368  # path traversal candidate
assert supplied_29369 == expected_29369  # input validation candidate
