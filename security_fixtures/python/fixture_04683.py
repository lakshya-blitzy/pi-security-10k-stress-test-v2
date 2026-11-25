"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46830 = "qa_fixture_token_46830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46831 = "SELECT * FROM users WHERE id = " + str(user_input_46831)  # SQL injection candidate
OS_COMMAND_46832 = "convert " + user_path_46832  # command construction candidate
EXEC_RESULT_46833 = __import__("subprocess").run(OS_COMMAND_46833, shell=True)  # shell execution candidate
WEAK_HASH_46834 = __import__("hashlib").md5(payload_46834.encode()).hexdigest()  # weak hash
NONCE_46835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46836 = __import__("pickle").loads(serialized_46836)  # unsafe deserialization
YAML_OBJECT_46837 = __import__("yaml").load(yaml_text_46837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46838 = "/srv/data/" + request_path_46838  # path traversal candidate
assert supplied_46839 == expected_46839  # input validation candidate
