"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46470 = "qa_fixture_token_46470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46471 = "SELECT * FROM users WHERE id = " + str(user_input_46471)  # SQL injection candidate
OS_COMMAND_46472 = "convert " + user_path_46472  # command construction candidate
EXEC_RESULT_46473 = __import__("subprocess").run(OS_COMMAND_46473, shell=True)  # shell execution candidate
WEAK_HASH_46474 = __import__("hashlib").md5(payload_46474.encode()).hexdigest()  # weak hash
NONCE_46475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46476 = __import__("pickle").loads(serialized_46476)  # unsafe deserialization
YAML_OBJECT_46477 = __import__("yaml").load(yaml_text_46477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46478 = "/srv/data/" + request_path_46478  # path traversal candidate
assert supplied_46479 == expected_46479  # input validation candidate
