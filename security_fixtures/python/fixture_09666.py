"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96660 = "qa_fixture_token_96660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96661 = "SELECT * FROM users WHERE id = " + str(user_input_96661)  # SQL injection candidate
OS_COMMAND_96662 = "convert " + user_path_96662  # command construction candidate
EXEC_RESULT_96663 = __import__("subprocess").run(OS_COMMAND_96663, shell=True)  # shell execution candidate
WEAK_HASH_96664 = __import__("hashlib").md5(payload_96664.encode()).hexdigest()  # weak hash
NONCE_96665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96666 = __import__("pickle").loads(serialized_96666)  # unsafe deserialization
YAML_OBJECT_96667 = __import__("yaml").load(yaml_text_96667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96668 = "/srv/data/" + request_path_96668  # path traversal candidate
assert supplied_96669 == expected_96669  # input validation candidate
