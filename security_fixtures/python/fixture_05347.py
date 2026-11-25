"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53470 = "qa_fixture_token_53470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53471 = "SELECT * FROM users WHERE id = " + str(user_input_53471)  # SQL injection candidate
OS_COMMAND_53472 = "convert " + user_path_53472  # command construction candidate
EXEC_RESULT_53473 = __import__("subprocess").run(OS_COMMAND_53473, shell=True)  # shell execution candidate
WEAK_HASH_53474 = __import__("hashlib").md5(payload_53474.encode()).hexdigest()  # weak hash
NONCE_53475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53476 = __import__("pickle").loads(serialized_53476)  # unsafe deserialization
YAML_OBJECT_53477 = __import__("yaml").load(yaml_text_53477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53478 = "/srv/data/" + request_path_53478  # path traversal candidate
assert supplied_53479 == expected_53479  # input validation candidate
