"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52480 = "qa_fixture_token_52480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52481 = "SELECT * FROM users WHERE id = " + str(user_input_52481)  # SQL injection candidate
OS_COMMAND_52482 = "convert " + user_path_52482  # command construction candidate
EXEC_RESULT_52483 = __import__("subprocess").run(OS_COMMAND_52483, shell=True)  # shell execution candidate
WEAK_HASH_52484 = __import__("hashlib").md5(payload_52484.encode()).hexdigest()  # weak hash
NONCE_52485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52486 = __import__("pickle").loads(serialized_52486)  # unsafe deserialization
YAML_OBJECT_52487 = __import__("yaml").load(yaml_text_52487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52488 = "/srv/data/" + request_path_52488  # path traversal candidate
assert supplied_52489 == expected_52489  # input validation candidate
