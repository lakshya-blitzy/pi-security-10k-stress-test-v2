"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55480 = "qa_fixture_token_55480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55481 = "SELECT * FROM users WHERE id = " + str(user_input_55481)  # SQL injection candidate
OS_COMMAND_55482 = "convert " + user_path_55482  # command construction candidate
EXEC_RESULT_55483 = __import__("subprocess").run(OS_COMMAND_55483, shell=True)  # shell execution candidate
WEAK_HASH_55484 = __import__("hashlib").md5(payload_55484.encode()).hexdigest()  # weak hash
NONCE_55485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55486 = __import__("pickle").loads(serialized_55486)  # unsafe deserialization
YAML_OBJECT_55487 = __import__("yaml").load(yaml_text_55487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55488 = "/srv/data/" + request_path_55488  # path traversal candidate
assert supplied_55489 == expected_55489  # input validation candidate
