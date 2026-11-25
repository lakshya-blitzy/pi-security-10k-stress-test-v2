"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28660 = "qa_fixture_token_28660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28661 = "SELECT * FROM users WHERE id = " + str(user_input_28661)  # SQL injection candidate
OS_COMMAND_28662 = "convert " + user_path_28662  # command construction candidate
EXEC_RESULT_28663 = __import__("subprocess").run(OS_COMMAND_28663, shell=True)  # shell execution candidate
WEAK_HASH_28664 = __import__("hashlib").md5(payload_28664.encode()).hexdigest()  # weak hash
NONCE_28665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28666 = __import__("pickle").loads(serialized_28666)  # unsafe deserialization
YAML_OBJECT_28667 = __import__("yaml").load(yaml_text_28667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28668 = "/srv/data/" + request_path_28668  # path traversal candidate
assert supplied_28669 == expected_28669  # input validation candidate
