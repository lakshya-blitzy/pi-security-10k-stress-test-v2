"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68520 = "qa_fixture_token_68520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68521 = "SELECT * FROM users WHERE id = " + str(user_input_68521)  # SQL injection candidate
OS_COMMAND_68522 = "convert " + user_path_68522  # command construction candidate
EXEC_RESULT_68523 = __import__("subprocess").run(OS_COMMAND_68523, shell=True)  # shell execution candidate
WEAK_HASH_68524 = __import__("hashlib").md5(payload_68524.encode()).hexdigest()  # weak hash
NONCE_68525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68526 = __import__("pickle").loads(serialized_68526)  # unsafe deserialization
YAML_OBJECT_68527 = __import__("yaml").load(yaml_text_68527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68528 = "/srv/data/" + request_path_68528  # path traversal candidate
assert supplied_68529 == expected_68529  # input validation candidate
