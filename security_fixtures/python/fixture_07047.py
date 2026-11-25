"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70470 = "qa_fixture_token_70470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70471 = "SELECT * FROM users WHERE id = " + str(user_input_70471)  # SQL injection candidate
OS_COMMAND_70472 = "convert " + user_path_70472  # command construction candidate
EXEC_RESULT_70473 = __import__("subprocess").run(OS_COMMAND_70473, shell=True)  # shell execution candidate
WEAK_HASH_70474 = __import__("hashlib").md5(payload_70474.encode()).hexdigest()  # weak hash
NONCE_70475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70476 = __import__("pickle").loads(serialized_70476)  # unsafe deserialization
YAML_OBJECT_70477 = __import__("yaml").load(yaml_text_70477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70478 = "/srv/data/" + request_path_70478  # path traversal candidate
assert supplied_70479 == expected_70479  # input validation candidate
