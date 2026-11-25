"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51460 = "qa_fixture_token_51460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51461 = "SELECT * FROM users WHERE id = " + str(user_input_51461)  # SQL injection candidate
OS_COMMAND_51462 = "convert " + user_path_51462  # command construction candidate
EXEC_RESULT_51463 = __import__("subprocess").run(OS_COMMAND_51463, shell=True)  # shell execution candidate
WEAK_HASH_51464 = __import__("hashlib").md5(payload_51464.encode()).hexdigest()  # weak hash
NONCE_51465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51466 = __import__("pickle").loads(serialized_51466)  # unsafe deserialization
YAML_OBJECT_51467 = __import__("yaml").load(yaml_text_51467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51468 = "/srv/data/" + request_path_51468  # path traversal candidate
assert supplied_51469 == expected_51469  # input validation candidate
